# 📈 Alpha Research VN

This project develops and backtests a quantitative **alpha model** for Vietnam's stock market, covering **1,327 equities** listed across **HOSE, HNX, and UPCOM** exchanges.

The strategy is built using **price–volume data** and fundamental indicators, trained on data from **early 2023 to present**, with separate in-sample (IS) and out-of-sample (OOS) backtests.

---

## 🚀 Performance Summary

### In-Sample (Training)
- **Annualized Return:** 51.69%  
- **Sharpe Ratio:** 3.59  
- **Max Drawdown:** −10.91%  

### Out-of-Sample (Backtest)
- **Annualized Return:** 63.03%  
- **Sharpe Ratio:** 3.14  
- **Max Drawdown:** −15.62%  

---

## 🧠 Project Overview
- Developed and validated an alpha model using both **technical** and **fundamental features**.  
- Conducted backtesting on over **1,300 listed stocks** using real Vietnam market data on HOSE, HNX, and
UPCOM exchange.  
- Designed a **custom research pipeline** for feature engineering, alpha scoring, and performance evaluation.  
- Collaborated with a **fundamental analyst** to refine trade logic, executing **3–5 trades per day** on average.  

---

## 💾 Data
Due to GitHub’s file size limits, large datasets are hosted externally.

| File | Description | Access |
|------|--------------|---------|
| `created_indicator.csv` | created_indicator | [Google Drive Link](https://drive.google.com/file/d/1iCese6w6B12u0Ad0_ktMqPjfozN_l-ri/view?usp=sharing) |
| `full_technical.csv` | Full technical indicator dataset | [Google Drive Link](https://drive.google.com/file/d/1_lNJmXMCvfoFN96CgnHDQDY81tayjDaO/view?usp=sharing) |
| `technical.csv` | Processed technical data | [Google Drive Link](https://drive.google.com/file/d/1j7J1K_6YbTCWIZuFnwN0_g1TM0k3mWqE/view?usp=sharing) |

---
## 📊 Strategy Performance

**In-Sample (Training) Result**
![In-Sample Result](https://drive.google.com/uc?export=view&id=1B5cFmrFiOzhS82gPyOhzmY2iA_PyFDRi)

**Out-of-Sample (Backtest) Result**
![Out-of-Sample Result](https://drive.google.com/uc?export=view&id=19adyHXGnZE8ScPV1Lsb1FX1dVjKU86zk)

---
## 🧩 Tech Stack
- **Python:** pandas, numpy, statsmodels, sklearn, matplotlib, CVXPY
- **Research tools:** Jupyter Notebook, Git, Google Colab  
- **Data sources:** Vietnam stock market price–volume & fundamentals data from FiinQuant
