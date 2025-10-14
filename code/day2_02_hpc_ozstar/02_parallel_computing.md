---
marp: true
theme: cn5_style
footer: slides by Lukas Steinwender
---

<!-- _class: titleslide -->
# Compute
## Parallel Computation and GPU

![bg](../../gfx/TitlePage.png)
<div class="footnote">Image generated with ChatGPT</div>

---
# Embarassingly Parallel Problems
* each task independent
* shared memory
* easy to parallelize

---
<!-- thread: each core can have several threads (each chrome tab is a thread) -->
# Threading
* easy to set up
* good for [embarassingly parallel problems](#embarassingly-parallel-problems)
* shared memory
* can only use a single machine
    * but multiple cores
* [Python](../day1_02_python/01_python_slides.md): [joblib](https://joblib.readthedocs.io)

---
# MPI (Message Passing Interface)
* more complex
* each process has its own memory
* can scale across multiple machines
* can adapt to more settings
* [Python](../day1_02_python/01_python_slides.md): [mpi4py](https://mpi4py.readthedocs.io/en/stable/)
    * requires [OpenMPI](https://docs.open-mpi.org/en/v5.0.x/index.html) to be installed
    * done for you on OzSTAR

```mermaid
flowchart LR
    main@{ shape: rounded, label: "Main"}
    worker1@{ shape: rounded, label: "Worker 1"}
    worker2@{ shape: rounded, label: "Worker 2"}
    workerN@{ shape: rounded, label: "Worker N"}
    out@{ shape: rect, label: "Output"}

    main -...->|assign work| worker1
    main -...->|assign work| worker2
    main -...->|assign work| workerN
    worker1 ---->|collect result| main
    worker2 ---->|collect result| main
    workerN ---->|collect result| main
    main ----->|combine results| out
```
---
# GPU Computing
<!-- TPU: Tensor Processing Unit -->
<!-- PPU: Physics Processing Unit -->
<div class="footnote">Image Credit: <a href=https://supercomputing.swin.edu.au/docs>Irfan et al., 2023</a></div>

![bg fit vertical right:30%](../../gfx/gpu_blockdiagram.png)

* GPU: highly specialized hardware
* designed for [embarassingly parallel problems](#embarassingly-parallel-problems)
* huge in Deep Learning
    * batch-wise gradient computation
* each block has it's own memory (shared across block)
    * each thread within a block has it's own local memory
* more specialized variants exist: TPU, PPU

> software needs to be designed for GPU-computation!

