# 📡 Telecom Customer Targeting (Machine Learning)
Predictive modelling project to identify customers most likely to take a **new mobile contract** in response to marketing — framed for telecom / fibre operators.

**Highlights**
- **Context**: Telecom marketing optimisation (reduce wasted calls, target likely converters).
- **Models**: Random Forest, Logistic Regression, Neural Network.
- **Result**: **AUC = 0.903**, **Accuracy = 0.889** (test); **Precision (YES) = 0.733**, **Recall (YES) = 0.618**.
- **Methodology**: CRISP‑DM with 5‑fold CV and manual hyper‑parameter tuning.
- **Data quality**: Fixed typoes (e.g., `cell`/`cellular`, `n`→`no`), handled class imbalance via oversampling.

> This repo is a *portfolio-ready* snapshot (no proprietary data). Add your own code/notebooks; keep credentials out of Git.

---

## 🧭 Project Overview
- **Business goal**: minimise campaign costs by prioritising customers likely to accept new contracts.
- **Target**: `new_contract_this_campaign` (YES/NO).
- **Key drivers (feature importance / IGR)**: `outcome_previous_campaign`, `last_contact`.

### Data (sample)
- Original dataset referenced in coursework (*not provided here*). Place a small sample (e.g., `data/sample.csv`) if needed for demo.
- Keep raw data **out of Git**. Use `.gitignore` and an `.env` if needed.

---

## 🏗️ Repository Structure
```
telecom-customer-targeting-ml/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ requirements.txt
├─ src/
│  ├─ __init__.py
│  └─ app.py                  # (optional) Streamlit demo placeholder
├─ notebooks/
│  └─ 01_exploration.ipynb    # put your notebook(s) here
├─ data/
│  └─ sample.csv              # tiny mock sample only (not real data)
├─ models/
│  └─ README.md               # notes on model artifacts (not tracked)
└─ docs/
   └─ poster-placeholder.png  # export your poster here (optional)
```

---

## 🚀 Quickstart
```bash
# 1) (optional) create & activate venv
python -m venv .venv
# Windows:
#   .venv\Scripts\activate
# macOS / Linux:
#   source .venv/bin/activate

# 2) install deps
pip install -r requirements.txt

# 3) run demo app (placeholder)
streamlit run src/app.py
```

---

## 📊 Modelling Summary (for reviewers)
- **Split**: Train 70% / Test 30%; **5‑fold CV** on train.
- **Class imbalance**: minority class oversampled.
- **Models + tuning (manual/random search)**:
  - **Random Forest**: `n_estimators=100`, `min_samples_split=2` → **best**
  - **Neural Network**: hidden layers `(200, 200)`, `tanh`, `adam`, `alpha=1e-4`, `max_iter=1200`
  - **Logistic Regression**: L2, `C=5`
- **Metric focus**: **Precision (YES)** to reduce wasted calls; tracked Recall & AUC for balance.

**Test confusion matrix (from coursework)**
- TP: 2,126 | TN: 11,685 | FP: 535 | FN: 852

---

## 🧪 Repro Notes
- Replace `data/sample.csv` with a synthetic or anonymised sample if you need to show code execution.
- Do **not** commit the real dataset or any API keys.
- If models are large, consider **Git LFS**.

---

## 📜 License
Released under the **MIT License** — see `LICENSE`.
