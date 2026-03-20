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

## Project Structure
- `data/`: sample data
- `src/`: preprocessing, feature engineering, and modeling scripts
- `notebooks/`: exploratory analyses
- `results/`: output figures and tables
- `docs/`: short project documentation
- `poster/`:project poster for conference/ regular sharing 

## Current Status
This is a minimal demonstration version designed to show the computational workflow for social-media-based mental health modeling.

## Methods
### The pipeline is designed to approximate how psychological processes can be operationalized from natural language data.

This repository includes:

1. Text preprocessing
2. Sentiment feature extraction e.g. VADER / LIWC-style variables
3. Temporal feature construction
4. Statistical modeling
   
### 1. Text Processing
- Tokenization and normalization of raw social media text
- Basic text cleaning and preprocessing

### 2.Lexicon-Based Sentiment Analysis
- Sentiment scoring using VADER (Valence Aware Dictionary and sEntiment Reasoner)
- Extraction of positive, negative, neutral, and compound sentiment scores
- Approximation of LIWC-style affective features

### 3.Temporal Feature Engineering
- Construction of longitudinal emotion trajectories per user
- Derivation of key temporal features:
  - Emotional amplitude (range of sentiment variation)
  - Emotional variability (standard deviation)
  - Emotional inertia (lag-1 autocorrelation)

### 4. Statistical Modeling
- Logistic regression for binary classification of depression risk
- Feature-based modeling linking temporal emotion dynamics to mental health outcomes

### Computational Framing
This pipeline reflects a computational approach to psychological processes, treating language as a behavioral signal and modeling mental states through time-series features extracted from naturalistic text data.


## Next Step( to be continue...)
- Larger-scale longitudinal datasets
- Linguistic agency and attributional style features
- Mixed-effects modeling
- Cross-platform comparison across Reddit, X, and Weibo

## Author
Yayun Zheng
MA Candidate in Psychology, New York University
