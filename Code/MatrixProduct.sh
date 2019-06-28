#!/usr/bin/sh

hadoop fs -rm -r /user/student/16081080/output/

hadoop jar /opt/apps/ecm/service/hadoop/2.8.5-1.2.0/package/hadoop-2.8.5-1.2.0/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar \
    -input /user/student/16081080/Matrix_try.txt \
    -output /user/student/16081080/output/ \
    -file mapper.py reducer.py \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \

