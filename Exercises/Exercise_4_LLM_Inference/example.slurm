#!/bin/bash

## General note: The more resources you request and the more resources you have requested in the past, the less priority you get in the queue.
## There is different queues/"partitions" with different waiting times available, so choose wisely. See what is available with sinfo_t_idle
## For more information, see: https://wiki.bwhpc.de/e/BwUniCluster3.0/Running_Jobs

#SBATCH --job-name=EXAMPLE1
#SBATCH --partition=dev_cpu_il  # choose your partition (you can check which ones are available with sinfo_t_idle)
#SBATCH --time=00:05:00  	# computing time, after this, your job will be terminated (dev/short queues only allow for 30 min)
#SBATCH --nodes=1  		# compute nodes, for most jobs one is enough
#SBATCH --ntasks=1  		# number of tasks across all nodes
##SBATCH --gres=gpu:1   # request a GPU only if you need it
#SBATCH --output="slurm_logs/example/%A.out" # writes the outputs of your job to a file
#SBATCH --error="slurm_logs/example/%A.err" # writes the errors of your job to another file
#SBATCH --mail-type=begin       # send email when job begins
#SBATCH --mail-type=end         # send email when job ends
#SBATCH --mail-type=fail        # send email when job fails
##SBATCH --mail-user=USERNAME@mail.uni-mannheim.de

#module load devel/cuda # For using the GPU

source ~/llm4ess_env/bin/activate # Activate the virtual environment – make sure the path is correct!

python example.py # Run your code here
