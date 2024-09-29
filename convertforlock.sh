#!/bin/bash

function help() {
    echo ""
    echo "usage:"
    echo "${0} (-e|-r) <input_file> <output_file>"
    echo "-e ... The option file format is conda environment.yml."
    echo "-r ... The option file format is requirements.txt."
    echo "<input_file>  ... It is a input file of exported conda environment."
    echo "<output_file> ... It is a output file for importing environment."
    echo "              ... format for conda environment."
    echo "              ... format for pip install."

}

function input_yesno() # 関数の宣言
{
    input=""

    while [[ ${input,,} != 'y' ]] && [[ ${input,,} != 'n' ]]
    do
        read -p 'Are you all right? [y/n]: ' input
    done
    if [[ ${input,,} = 'n' ]]; then
        echo "It is canceled."
        exit 1
    fi
}

function output_yml() {
    echo "conda environment format: $1 >> $2"
    echo "if you have these files, there will be overwritten."
    input_yesno
    # remove library suffix.
    cat $1 | sed -E "s/^[ -]+([-_\.\+a-zA-Z0-9]+[=$\n\r\f]{1}[-!_\.\+a-zA-Z0-9]*)[$ =]?[=_\.\+a-zA-Z0-9]+$/  - \1/" | sed -e '$d' > $2
}

function output_txt() {
    echo "pip install format: $1 >> $2"
    echo "if you have these files, there will be overwritten."
    input_yesno
    # remove library suffix.
    cat $1 | sed -E "s/^([-_.\+a-zA-Z0-9]+[\=$\n\r\f\]?[\!-_.+a-zA-Z0-9]*)[ =]+[\=_.+a-zA-Z0-9]+$/\1/" > $2
}

# start main process
echo ""
cnt=0;
opts_list=()
while getopts "hre-" type_opt
do
    cnt+=1;
    if [ $cnt -ge 2 ]; then
        echo "Input error - The option is only one choice."
        help
        exit 1
    fi
    opts_list+=( "${type_opt}" )
done

input_file=$2
output_file=$3

if [ -z ${input_file} ] || [ -z ${output_file} ]; then
    echo "please specify a option, a input file and a output file."
    help
    exit 1
fi

for type in $opts_list
do
    case "${type}" in
        h)
            help
            exit 0
            ;;
        e)
            # environment.yml形式ファイルの場合
            echo "e"
            output_yml $input_file $output_file
            ;;
        r)
            # requirements.txt形式ファイルの場合
            echo "r"
            output_txt $input_file $output_file
            ;;
        *)
            echo "other"
            help
            exit 1
            ;;
        \?)
            echo "?"
            help
            exit 1
            ;;
    esac
done

echo "done."
