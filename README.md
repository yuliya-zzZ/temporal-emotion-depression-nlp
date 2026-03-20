# Temporal Emotion Depression NLP

A minimal NLP pipeline for modeling temporal emotion dynamics in social media text and predicting depression risk.

## Project Overview
This project implements a small-scale computational pipeline to analyze longitudinal social media text and extract temporal emotional features related to depression risk.

The project is based on the idea that depression is reflected not only in average negative sentiment, but also in how emotion unfolds over time, including:

- emotional amplitude
- emotional variability
- emotional inertia

## Research Motivation
Prior work suggests that persistent negative emotion and reduced linguistic agency may serve as markers of depression risk. This project builds a lightweight pipeline to operationalize these constructs using social media text.

## Methods
This repository includes:

1. Text preprocessing
2. Sentiment feature extraction using VADER / LIWC-style variables
3. Temporal feature construction
4. A baseline prediction model for depression risk

## Project Structure
- `data/`: sample data
- `src/`: preprocessing, feature engineering, and modeling scripts
- `notebooks/`: exploratory analyses
- `results/`: output figures and tables
- `docs/`: short project documentation

## Current Status
This is a minimal demonstration version designed to show the computational workflow for social-media-based mental health modeling.

## Future Extensions
- Larger-scale longitudinal datasets
- Linguistic agency and attributional style features
- Mixed-effects modeling
- Cross-platform comparison across Reddit, X, and Weibo

## Author
Yayun Zheng
MA Candidate in Psychology, New York University
