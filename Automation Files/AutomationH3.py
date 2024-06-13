import os
import shutil
import subprocess

# Define cache configuration parameters
cache_line_sizes = [64]
l1d_associativity = [2]
l1i_associativity=[1,2,4,8]
l2_associativity=[1]
l1d_cache_sizes = [128]
l1i_cache_sizes = [128]
l2_cache_sizes = [1]

# Specify the benchmark directory and CPU type
benchmark_path = "/home/013/a/ax/axb230073/CA_Project2/Project1_SPECMASTER/458.sjeng"
cpu_model = "timing"

# Iterate over cache configurations and run simulations
for cache_line_size in cache_line_sizes:
    for l1d_assoc in l1d_associativity :
        for l1i_assoc in l1i_associativity:
            for l2_assoc in l2_associativity:
                for l1d_size in l1d_cache_sizes:
                    for l1i_size in l1i_cache_sizes:
                        for l2_size in l2_cache_sizes:
                            # Set the output directory path
                            output_dir = "/home/013/a/ax/axb230073/CA_Project2/OutputS3/458.sjeng/458_{}-{}-{}-{}-{}-{}-{}".format(cache_line_size, l1d_assoc, l1i_assoc, l2_assoc, l1d_size, l1i_size, l2_size)


                            if os.path.exists(output_dir):
                                shutil.rmtree(output_dir)

                            # Create a new directory for the current configuration
                            os.makedirs(output_dir)

                            # Construct the command to run the gem5 simulation
                            gem5_command = "./build/X86/gem5.opt -d {} ".format(output_dir) + \
                                    "./configs/example/se.py -c {}/src/benchmark ".format(benchmark_path) + \
                                    "-o {}/data/test.txt -I 50000000 ".format(benchmark_path) + \
                                    "--cpu-type={} --caches --l2cache ".format(cpu_model) + \
                                    "--l1d_size={}kB --l1i_size={}kB ".format(l1d_size, l1i_size) + \
                                    "--l2_size={}MB --l1d_assoc={} ".format(l2_size, l1d_assoc) + \
                                    "--l1i_assoc={} --l2_assoc={} ".format(l1i_assoc, l2_assoc) + \
                                    "--cacheline_size={}".format(cache_line_size)



                            

                            # Change to the gem5 directory and execute the simulation
                            os.chdir("/home/013/a/ax/axb230073/CA_Project2/gem5")
                            os.system(gem5_command)