# Computer_ArchitectureProject
## Project Overview

Our project involves a detailed exploration and optimization of the cache hierarchy in the x86 architecture using the gem5 simulator. We perform comprehensive benchmarks to find the optimal Cache Per Instruction (CPI) and analyze cost functions for cache configurations.

### Objectives
- Calculate the CPI for a set of benchmarks.
- Optimize the CPI for each benchmark.
- Define and implement a cost function for the caches.
- Analyze trade-offs between CPI and cache parameters.

### Tools Used
- **gem5 Simulator**: Main simulation tool used for this project.
- **Benchmarks**: 456.hmmer and 458.sjeng.

## Setup and Running Simulations

1. **Initial Setup**:
    - Clone the repository to the local system.
    - Ensure gem5 and all dependencies are correctly installed.

2. **Running Benchmarks**:
    - Scripts are provided in the `Scripts/` directory to run the benchmarks.
    - Use the `runGem5.sh` script to initiate the simulation environment.

## Results and Analysis

- **CPI Calculation**:
    - Detailed calculations of CPI for benchmarks are included, analyzing the efficiency of processor instructions execution.
- **Optimization**:
    - The optimal cache configurations to achieve the lowest CPI are identified and detailed.

- **Cost Analysis**:
    - A cost function is defined and used to evaluate different cache configurations, balancing performance and cost.

## Graphs

- Visual representations of CPI vs Cost trade-offs are provided in the `Graphs/` directory, helping to visualize performance impacts due to changes in cache parameters.

## Conclusion

This project demonstrates the effectiveness of various cache configurations and their impact on system performance, providing valuable insights into architectural choices in CPU design.


