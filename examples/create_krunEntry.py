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
        .param("program", new String[] {{ "/home/benchmarks/jvms/{name}.xmi" }})
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

tmp = MODEL.format(fullQualifiedInterpreter="test_FQN", name="test_name")

print(tmp)
"fr.mleduc.boa.BoaInterpreterBenchmark.boaInterpreter"
