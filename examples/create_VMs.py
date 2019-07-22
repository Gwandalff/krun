from distutils.spawn import find_executable

JAVA_BIN = find_executable("java")

print(JAVA_BIN)

JVMS_FOLDER = "/home/benchmarks/jvms/"
BENCH_FOLDER = "/home/benchmarks/benchmark/"

VMS = {}
SKIP = []

jvms = ["hotspot-8u222-b10", "hotspot_11.0.4", "hotspot_12.0.2", "openj9_8u222-b10", "openj9_11.0.4", "openj9_12.0.1", "graalvm-ce-19.1.1", "graalvm-ee-19.1.1"]

languages = ["boa", "fsm", "logo", "minijava"]

# wait for the maven install of the truffle benchmarks
patterns = ["interpreter", "revisitor", "switch", "visitor"]
#patterns = ["interpreter", "revisitor", "switch", "visitor", "truffle"]

BENCHMARKS = {
    'boa_interpreter_fib': 2,
}

for jvm in jvms:
	for lang in languages:
		for pattern in patterns:
			name = lang + "_" + pattern + "_" + jvm
			krun_vm = {
				#'vm_def': JavaJarVMDef(JVMS_FOLDER+jvm+".jar", BENCH_FOLDER+lang+"/"+pattern+"/benchmarks.jar"),
				'JAVA_BIN': JVMS_FOLDER+jvm+"/bin/java",
				'Bench' : BENCH_FOLDER+lang+"/"+pattern+"/benchmarks.jar",
        			'variants': ['default-java'],
        			'n_iterations': 1#ITERATIONS_ALL_VMS,
			}
			VMS[name] = krun_vm
			for bench in BENCHMARKS:
				if lang not in bench or (pattern == "truffle" and "graal" not in jvm):
					SKIP.append(str(bench)+":"+str(name)+":*")

for key in VMS:
	print(key + " : ")
	print(VMS[key])

for s in SKIP:
	print(s)



