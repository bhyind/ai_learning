# AI Learning Journey

A hands-on project for learning how modern AI systems work from the ground up.

The goal is to progress from basic tensor operations to running, understanding, fine-tuning, evaluating, and eventually integrating AI models with real-world systems such as robotics.

## Hardware

- Intel Core Ultra 9 275HX
- 32 GB RAM
- NVIDIA GeForce RTX 5060 Laptop GPU
- 8 GB VRAM

## Development Environment

- Windows 11
- WSL2
- Ubuntu
- Python
- PyTorch
- CUDA
- Hugging Face
- VS Code
- Git / GitHub

## Learning Roadmap

### Foundations

- [ ] 01 — Python and PyTorch
- [x] 02 — Tensors and CUDA
- [ ] 03 — Tokenization
- [ ] 04 — Embeddings
- [ ] 05 — Transformers
- [ ] 06 — Model Inference
- [ ] 07 — Prompting

### AI Systems

- [ ] 08 — Retrieval-Augmented Generation (RAG)
- [ ] 09 — Fine-Tuning
- [ ] 10 — LoRA and QLoRA
- [ ] 11 — Model Evaluation
- [ ] 12 — Agents and Tool Use

### Advanced AI

- [ ] 13 — Multimodal Models
- [ ] 14 — Robotics Foundations

## Completed Experiment: CPU vs GPU

Using PyTorch, a 6000 × 6000 matrix multiplication was performed on both the CPU and GPU.

| Device | Time |
|---|---:|
| CPU | 0.295 seconds |
| RTX 5060 GPU | 0.051 seconds |

GPU speedup: **5.8×**

This demonstrated that PyTorch can move tensors into GPU memory and use CUDA for parallel computation.

## Repository Structure

- `foundations/` — individual concepts and experiments
- `projects/` — complete AI applications
- `src/` — reusable Python code
- `notebooks/` — exploratory work
- `configs/` — configuration files
- `data/` — datasets
- `models/` — locally stored models
- `outputs/` — generated results
- `tests/` — automated tests
- `docs/` — longer-form documentation

## Current Focus

Tokenization: understanding how text becomes numeric input that a language model can process.