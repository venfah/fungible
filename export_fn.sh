
# shell script to do csv data of some functions

final_str='';
i=0
for each_fn in $(mdcap fn list | cut -d" " -f1 | grep -P "^[a-f\d]+");
do
        echo $each_fn;
        if [ $i -eq 0 ];
        then
                final_str="${each_fn}";
        else
                final_str="${final_str},${each_fn}";
        fi
        i=$((i+1))
done
mdcap fn export ${final_str} /tmp/functions1.tar.gz
