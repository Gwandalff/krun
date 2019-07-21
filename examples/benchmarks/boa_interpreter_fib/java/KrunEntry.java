import org.openjdk.jmh.results.format.ResultFormatType;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.ChainedOptionsBuilder;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

public class KrunEntry
  implements BaseKrunEntry
{
  public void run_iter(int param)
  {
    Options opt = new OptionsBuilder()
        .include("fr.mleduc.boa.BoaInterpreterBenchmark.boaInterpreter")
        .forks(1)
        .warmupIterations(0)
        .measurementIterations(param)
        .resultFormat(ResultFormatType.JSON)
        .result("/tmp/boa_interpreter_fib_" + System.currentTimeMillis() + ".json")
        .param("program", new String[] { "/home/mleduc/krun/examples/benchmarks/boa_interpreter_fib/boa_fibonacci.xmi" })
        .build();
    try
    {
      new Runner(opt).run();
    }
    catch (RunnerException e)
    {
      e.printStackTrace();
    }
  }
}
