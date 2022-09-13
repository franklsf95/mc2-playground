## TPC-DS Spark

[http://www.openkb.info/2021/02/how-to-generate-tpc-ds-data-and-run-tpc.html](http://www.openkb.info/2021/02/how-to-generate-tpc-ds-data-and-run-tpc.html)

Generate data:

```bash
spark-shell --driver-memory 16g --jars /home/ubuntu/spark-sql-perf/target/scala-2.12/spark-sql-perf_2.12-0.5.1-SNAPSHOT.jar -i scripts/gendata.scala
```

Run benchmark:

```bash
spark-shell --driver-memory 16g --jars /home/ubuntu/spark-sql-perf/target/scala-2.12/spark-sql-perf_2.12-0.5.1-SNAPSHOT.jar -i scripts/run.scala
```

Get results:

```bash
experiment.getCurrentResults.createOrReplaceTempView("result")
sql("select substring(name,1,100) as Name, bround((parsingTime+analysisTime+optimizationTime+planningTime+executionTime)/1000.0,1) as Runtime_sec from result").show()
sql("select sum(parsingTime+analysisTime+optimizationTime+planningTime+executionTime) from result").show()
```

Fix ulimits

```bash
sudo bash -c 'rm -rf /etc/security/limits.d; echo "* soft nofile 65535" >> /etc/security/limits.conf; echo "* hard nofile 65535" >> /etc/security/limits.conf;'
```

## Results (SF=2)

Graviton: 468.067s (10% faster)

Intel: 517.558s

Graviton:

```bash
+---------+-----------+
|     Name|Runtime_sec|
+---------+-----------+
|  q1-v2.4|        5.1|
|  q2-v2.4|        4.4|
|  q3-v2.4|        0.9|
|  q4-v2.4|       17.2|
|  q5-v2.4|        5.0|
|  q6-v2.4|        3.2|
|  q7-v2.4|        1.4|
|  q8-v2.4|        2.0|
|  q9-v2.4|        9.8|
| q10-v2.4|        5.6|
| q11-v2.4|        8.5|
| q12-v2.4|        1.3|
| q13-v2.4|        1.4|
|q14a-v2.4|       23.1|
|q14b-v2.4|       16.6|
| q15-v2.4|        0.9|
| q16-v2.4|        6.0|
| q17-v2.4|        3.5|
| q18-v2.4|        2.3|
| q19-v2.4|        1.0|
+---------+-----------+
```

Intel:

```bash
+---------+-----------+
|     Name|Runtime_sec|
+---------+-----------+
|  q1-v2.4|        5.4|
|  q2-v2.4|        4.8|
|  q3-v2.4|        1.0|
|  q4-v2.4|       19.4|
|  q5-v2.4|        4.9|
|  q6-v2.4|        3.4|
|  q7-v2.4|        1.5|
|  q8-v2.4|        1.8|
|  q9-v2.4|       10.3|
| q10-v2.4|        5.6|
| q11-v2.4|        9.8|
| q12-v2.4|        1.2|
| q13-v2.4|        1.3|
|q14a-v2.4|       26.1|
|q14b-v2.4|       18.2|
| q15-v2.4|        0.8|
| q16-v2.4|        6.7|
| q17-v2.4|        3.7|
| q18-v2.4|        2.5|
| q19-v2.4|        0.9|
+---------+-----------+
```

SF=100 and SF=1000 experiments Results: [https://docs.google.com/spreadsheets/d/1cwfFAVMjNk4nkfCH8k18j57jqDxKcR_wq3N-7AVSOvI/edit#gid=2136951180](https://docs.google.com/spreadsheets/d/1cwfFAVMjNk4nkfCH8k18j57jqDxKcR_wq3N-7AVSOvI/edit#gid=2136951180)
