# 🛡️ Contact Validator — CI/CD Pipeline & Quality Gate Scenario

[![Run Tests](https://github.com/atharva635/contact-validator-scenario/actions/workflows/test.yml/badge.svg)](https://github.com/atharva635/contact-validator-scenario/actions/workflows/test.yml)
[![Enforce Coverage](https://github.com/atharva635/contact-validator-scenario/actions/workflows/coverage.yml/badge.svg)](https://github.com/atharva635/contact-validator-scenario/actions/workflows/coverage.yml)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Test Suite: Pytest](https://img.shields.io/badge/Tested%20with-Pytest-0A9EDC.svg?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Code Coverage: ≥85%](https://img.shields.io/badge/Coverage-Enforced%20%E2%89%A585%25-brightgreen.svg?logo=codecov&logoColor=white)](https://pytest-cov.readthedocs.io/)
[![Branch Protection: Enabled](https://img.shields.io/badge/Branch%20Protection-main%20(Ruleset)-orange.svg?logo=github)](https://github.com)

> A real-world Continuous Integration (CI) and Quality Assurance practical implementation demonstrating how automated test suites, strict code-coverage gating, and GitHub branch protection rulesets block untested or breaking changes from entering production branches.

---

## 📑 Table of Contents

- [🎯 Executive Summary & Objectives](#-executive-summary--objectives)
- [🏗️ Repository Architecture](#️-repository-architecture)
- [🐍 Application Features](#-application-features)
- [🔄 End-to-End CI Pipeline Flow](#-end-to-end-ci-pipeline-flow)
- [⚙️ GitHub Actions Workflow Specifications](#️-github-actions-workflow-specifications)
- [🔐 Branch Protection & Quality Gate Mechanism](#-branch-protection--quality-gate-mechanism)
- [💥 The Real-World Failure & TDD Recovery Journey](#-the-real-world-failure--tdd-recovery-journey)
- [🚀 Local Setup & Development](#-local-setup--development)
- [🧠 Key Learnings & Interview/Viva Q&A](#-key-learnings--interviewviva-qa)
- [🛠️ Tech Stack](#️-tech-stack)

---

## 🎯 Executive Summary & Objectives

In modern DevOps and software engineering workflows, deploying code directly or merging unverified Pull Requests (PRs) poses severe stability risks. This repository simulates an enterprise-grade CI environment designed to:

1. **Automate Quality Checks:** Trigger dual isolated CI workflows on every Pull Request targeting the `main` branch.
2. **Enforce Coverage Thresholds:** Mandate a non-negotiable **85% code coverage threshold** exclusively over the `src/` application module.
3. **Hard-Gating with Rulesets:** Implement GitHub Branch Protection Rulesets to programmatically lock the `main` branch against direct pushes and failing PRs.
4. **Demonstrate Failure Recovery:** Showcase an intentional coverage failure diagnosis (`74% ➔ 83% ➔ 85%+`) and resolution process.

---

## 🏗️ Repository Architecture

```text
contact-validator-scenario/
├── .github/
│   └── workflows/
│       ├── test.yml          # Workflow A: Automated unit testing via Pytest
│       └── coverage.yml      # Workflow B: Code coverage enforcement (--cov-fail-under=85)
├── src/
│   ├── __init__.py
│   └── contact_validator.py  # Core business logic (Email/Phone validators & transformers)
├── tests/
│   ├── __init__.py
│   └── contact_validator_test.py # Unit tests covering regular & edge cases
├── .gitignore
├── requirements.txt          # Python dependencies (pytest, pytest-cov)
└── README.md                 # Complete documentation & runbooks
