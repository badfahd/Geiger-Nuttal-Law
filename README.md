# Geiger-Nuttall Law Visualization

A Python script to calculate alpha particle ranges ($R$) from radioactive decay constants ($\lambda$) using empirical Geiger-Nuttall parameters and visualize the linear log-log relationship across natural radioactive series.

---

## 📌 Overview
The **Geiger-Nuttall law** establishes a linear relationship between the logarithm of the radioactive decay constant ($\lambda$) and the logarithm of the range ($R$) of emitted alpha particles in air:

$$\log_{10}(\lambda) = A + B \log_{10}(R)$$

This script models this relationship for the three major natural radioactive series:
* **Uranium Series**
* **Thorium Series**
* **Actinium Series**

---

## 🚀 Features
* **Custom Calculation Function:** Computes alpha particle range ($R$) dynamically from known decay constants ($\lambda$) using series-specific intercept ($A$) and slope ($B$) constants.
* **Automated Data Processing:** Loops through multiple isotope datasets, computes ranges, and applies base-10 logarithmic transformations.
* **Comparative Visualization:** Generates a clean, color-coded Matplotlib scatter and line plot showing the nearly parallel trends across all three series.

---
#OUTPUT:<img width="900" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/782f4fab-d977-42de-b11d-9f9a546686ce" />


## 🛠️ Prerequisites & Dependencies
Make sure you have Python installed along with the required libraries:

```bash
pip install numpy matplotlib
