import os
import cv2

class Separator():
    def __init__(self, *args, **kwargs):
        """
        This is origin and target image infomation.
        params
            target: target image file path.
        """
        self.input_file = kwargs['input_file']

    def separate(self, h_num, w_num, out_file=None):
        """
        This is origin and target image infomation.
        params
            h_num: vertical separated file count.
            w_num: horizontal separated file count.
            out_file: separated image file path.
        """
        out_file = os.path.join("split_{:010}.png") if out_file is None else out_file

        # Read origin image.
        img = cv2.imread(self.input_file)
        height, width, channels = img.shape

        # Define separated size.
        h_split_size = int(height / h_num)
        w_split_size = int(width / w_num)

        img_num = 1
        for h in range(h_num):
            # Get target image of separated height.
            h_start = h * h_split_size
            h_end = h_start +  h_split_size

            for w in range(w_num):
                # Get target image of separated width.
                w_start = w * w_split_size
                w_end = w_start +  w_split_size

                # Output target image file.
                file_name = out_file.format(img_num)
                clp = img[h_start:h_end, w_start:w_end]
                cv2.imwrite(file_name, clp)
                img_num += 1
