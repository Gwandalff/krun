import os
import subprocess

MODEL = '''import org.openjdk.jmh.results.format.ResultFormatType;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.ChainedOptionsBuilder;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

public class KrunEntry
  implements BaseKrunEntry
{{
  public void run_iter(int param)
  {{
    Options opt = new OptionsBuilder()
        .include("{fullQualifiedInterpreter}")
        .forks(1)
        .warmupIterations(0)
        .measurementIterations(param)
        .resultFormat(ResultFormatType.JSON)
        .result("/home/benchmarks/results/{name}_" + System.currentTimeMillis() + ".json")
        .param("program", new String[] {{ "/home/benchmarks/programs/{name}.xmi" }})
        .build();
    try
    {{
      new Runner(opt).run();
    }}
    catch (RunnerException e)
    {{
      e.printStackTrace();
    }}
  }}
}}'''

def extractTestName(name):
	parts = name.split(".")
	return parts[0]

patterns = ["interpreter", "revisitor", "switch", "visitor"]

BENCH_FOR_JMH = "/home/benchmarks/benchmark/boa/interpreter/benchmarks.jar"

testNames = map(extractTestName, os.listdir("/home/benchmarks/programs/"))

benchs = []

for testName in testNames:
	testInfos = testName.split("_")
	lang = testInfos[0]
	test = testInfos[1]

	for pattern in patterns:
		krunName = lang+"_"+pattern+"_"+test
		benchs.append(krunName)
		KRUN_ENTRY_DIR = "./benchmarks/"+krunName+"/java/"
	
		if not os.path.exists(KRUN_ENTRY_DIR):
			os.makedirs(KRUN_ENTRY_DIR)
			
		f= open(KRUN_ENTRY_DIR+"KrunEntry.java","w+",0)
		
		fqn = "fr.mleduc." + lang + "." + lang.capitalize() + pattern.capitalize()+ "Benchmark." + lang + "Interpreter"

		tmp = MODEL.format(fullQualifiedInterpreter=fqn, name=krunName)
		f.write(tmp)
		f.close

		javac = ["javac","-cp",BENCH_FOR_JMH+":../iterations_runners/", KRUN_ENTRY_DIR+"KrunEntry.java"]
		rm = ["rm", KRUN_ENTRY_DIR+"KrunEntry.java"]
		proc = subprocess.Popen(javac)
		proc.wait()
		subprocess.Popen(rm)

f = open("bench_list.txt","w+",0)
f.write(";".join(benchs))
f.close()





