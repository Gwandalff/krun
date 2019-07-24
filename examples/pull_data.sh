while [ true ]
do
	scp benchmarks@buis.irisa.fr:/home/benchmarks/krun/examples/benchmarks* ./pulled_data/
	mv ./pulled_data/benchmarks.log ./pulled_data/benchmarks_$(date +%s).log
	mv ./pulled_data/benchmarks.manifest ./pulled_data/benchmarks_$(date +%s).manifest
	mv ./pulled_data/benchmarks_results.json.bz2 ./pulled_data/benchmarks_results_$(date +%s).json.bz2
	sleep 20
done
