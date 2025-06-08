# LoanSage: AI-Powered Loan Eligibility Predictor

A sophisticated web application that leverages machine learning to provide instant loan eligibility predictions. By analyzing key financial and demographic factors, LoanSage offers users quick insights into their loan approval chances.

## 🌟 Features

- **Real-time Predictions**: Instant loan eligibility assessment
- **Machine Learning Powered**: Utilizes decision tree algorithms for accurate predictions
- **User-friendly Interface**: Simple and intuitive web interface
- **Comprehensive Analysis**: Detailed insights into loan approval factors
- **Data Visualization**: Interactive charts and statistical analysis

## 📊 Key Insights

- **Eligibility Rate**: Approximately 29.5% of applicants qualify for loans
- **Income Correlation**: Higher income levels show stronger correlation with loan approval
- **Age Distribution**: Applicants range from 18 to 59 years
- **Loan Amount Range**: $5,097 to $49,976

## 🛠️ Technical Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Model Persistence**: pickle5

## 📋 Requirements

All required packages are listed in `requirements.txt`. To install them, run:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/prachi9695loansage.git
   cd loansage
   ```

2. **Set up virtual environment and install dependencies**
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   .\venv\Scripts\activate  # On Windows

   # Upgrade pip and install build tools
   python -m pip install --upgrade pip
   pip install wheel setuptools Cython

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Run the application locally**
   ```bash
   python app.py
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 🌐 GitHub Pages Deployment

The application is automatically deployed to GitHub Pages when changes are pushed to the main branch. The site is available at: `https://[your-username].github.io/loansage/`

To manually deploy:

1. **Build static files**
   ```bash
   python build_static.py
   ```

2. **Commit and push changes**
   ```bash
   git add .
   git commit -m "Update static files"
   git push origin main
   ```

The GitHub Actions workflow will automatically build and deploy your site to GitHub Pages.

## 📈 Statistical Overview

| Metric    | Age    | Income     | Loan Amount | Eligible |
|-----------|--------|------------|-------------|----------|
| Mean      | 38.75  | 69,785.69  | 27,816.92   | 0.295    |
| Std Dev   | 12.19  | 28,440.13  | 12,771.70   | 0.46     |
| Min       | 18.0   | 20,060.0   | 5,097.0     | 0.0      |
| Median    | 40.0   | 69,210.5   | 28,562.0    | 0.0      |
| Max       | 59.0   | 119,986.0  | 49,976.0    | 1.0      |

## 📊 Data Visualization

The application provides comprehensive visualizations:

- **Distribution Analysis**: Histograms for age, income, and loan amount
- **Income vs. Eligibility**: Boxplots showing the relationship between income and loan approval
- **Interactive Charts**: Real-time visualization of prediction results

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---

Made with ❤️ by Prachi Trivedi 