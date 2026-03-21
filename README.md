# Temporal Emotion Depression NLP

## Overview

This project implements an end-to-end NLP pipeline to analyze temporal emotional dynamics in social media text and predict depression risk.

The pipeline integrates psycholinguistic analysis (LIWC-style features), sentiment modeling (VADER), and statistical modeling (mixed-effects models) to study how emotional patterns over time relate to mental health outcomes.

Note: This project uses simulated data to validate the full analytical pipeline and research design. The focus is on modeling approach and computational workflow rather than empirical results.

The project is based on the idea that depression is reflected not only in average negative sentiment, but also in how emotion unfolds over time, including:

- emotional amplitude  
- emotional variability  
- emotional inertia  



## Research Motivation

Prior work suggests that persistent negative emotion and reduced linguistic agency may serve as markers of depression risk. This project operationalizes these constructs using social media text.



## Project Structure

- `data/`: sample data  
- `src/`: preprocessing, feature engineering, and modeling scripts  
- `notebooks/`: exploratory analyses  
- `results/`: output figures and tables  
- `docs/`: short project documentation  
- `poster/`: project poster for conference or general presentation  



## Current Status

This is a minimal demonstration version designed to illustrate the computational workflow for social-media-based mental health modeling.


## Methods

### The pipeline is designed to approximate how psychological processes can be operationalized from natural language data.

This repository includes:

1. Text preprocessing  
2. Sentiment feature extraction (e.g., VADER / LIWC-style variables)  
3. Temporal feature construction  
4. Statistical modeling  



### 1. Text Processing

- Tokenization and normalization of raw social media text  
- Basic text cleaning and preprocessing  



### 2. Lexicon-Based Sentiment Analysis

- Sentiment scoring using VADER (Valence Aware Dictionary and sEntiment Reasoner)  
- Extraction of positive, negative, neutral, and compound sentiment scores  
- Approximation of LIWC-style affective features  



### 3. Temporal Feature Engineering

- Construction of longitudinal emotion trajectories per user  
- Derivation of key temporal features:  
  - Emotional amplitude (range of sentiment variation)  
  - Emotional variability (standard deviation)  
  - Emotional inertia (lag-1 autocorrelation)  



### 4. Statistical Modeling

- Logistic regression for binary classification of depression risk  
- Feature-based modeling linking temporal emotion dynamics to mental health outcomes  



## Computational Framing

This pipeline reflects a computational approach to psychological processes, treating language as a behavioral signal and modeling mental states through time-series features extracted from naturalistic text data.



## Next Steps

- Apply to larger-scale longitudinal datasets  
- Incorporate linguistic features of agency and attributional style  
- Extend to mixed-effects modeling  
- Compare patterns across platforms (Reddit, X, Weibo)  



## Author
Yayun Zheng  
MA Candidate in Psychology, New York University
