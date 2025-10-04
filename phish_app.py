from flask import Flask, render_template, request
import pickle
import numpy as np
import re

# Initialize Flask app
phish_app = Flask(__name__)

# Load the trained model
try:
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
        print(f"Model loaded successfully. Expects {model.n_features_in_} features.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Feature extraction function
def extract_features(url):
    """
    Extracts numerical features from a given URL.
    """
    if not isinstance(url, str) or not url.startswith("http"):
        return None
    
    features = [
       1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0,  # IpAddress
        url.count('.'),  # NumDots
        url.count('.') - 1,  # SubdomainLevel
        url.count('/'),  # PathLevel
        len(url),  # UrlLength
        url.count('-'),  # NumDash
        url.split('/')[2].count('-') if len(url.split('/')) > 2 else 0,  # NumDashInHostname
        url.count('@'),  # AtSymbol
        url.count('~'),  # TildeSymbol
        url.count('_'),  # NumUnderscore
        url.count('%'),  # NumPercent
        url.count('?'),  # NumQueryComponents
        url.count('&'),  # NumAmpersand
        url.count('#'),  # NumHash
        sum(c.isdigit() for c in url),  # NumNumericChars
        1 if 'https' not in url.lower() else 0,  # NoHttps
        1 if re.search(r'[A-Za-z]{10,}', url) else 0,  # RandomString
        1 if len(url.split('/')[2].split('.')) > 2 else 0,  # DomainInSubdomains
        1 if '/' in url.split('/')[2] else 0,  # DomainInPaths
        1 if 'https' in url.split('/')[2].lower() else 0,  # HttpsInHostname
        len(url.split('/')[2]) if len(url.split('/')) > 2 else 0,  # HostnameLength
        len(url.split('/')) - 3,  # PathLength
        len(url.split('?')[-1]) if '?' in url else 0,  # QueryLength
        1 if '//' in url[8:] else 0,  # DoubleSlashInPath
        
        # Placeholder values (need proper calculation based on full dataset)
        0,  # NumSensitiveWords
        0,  # EmbeddedBrandName
        0,  # PctExtHyperlinks
        0,  # PctExtResourceUrls
        0,  # ExtFavicon
        0,  # InsecureForms
        0,  # RelativeFormAction
        0,  # ExtFormAction
        0,  # AbnormalFormAction
        0,  # PctNullSelfRedirectHyperlinks
        0,  # FrequentDomainNameMismatch
        0,  # FakeLinkInStatusBar
        0,  # RightClickDisabled
        0,  # PopUpWindow
        0,  # SubmitInfoToEmail
        0,  # IframeOrFrame
        0,  # MissingTitle
        0,  # ImagesOnlyInForm
        0,  # SubdomainLevelRT
        0,  # UrlLengthRT
        0,  # PctExtResourceUrlsRT
        0,  # AbnormalExtFormActionR
        0,  # ExtMetaScriptLinkRT
        0   # PctExtNullSelfRedirectHyperlinksRT
    ]
    
    features_array = np.array([features], dtype=np.float64)
    print(f"Extracted {len(features)} features: {features_array}")
    return features_array

# Route for the home page
@phish_app.route("/")
def home():
    return render_template("index.html")

# Route for prediction
@phish_app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return render_template("index.html", prediction_text="Error: Model not loaded!")

    try:
        url = request.form["url"].strip()
        print(f"URL entered: {url}")

        features_array = extract_features(url)
        if features_array is None:
            return render_template("index.html", prediction_text="Error: Invalid URL format.")
        
        if features_array.shape[1] != model.n_features_in_:
            return render_template(
                "index.html", 
                prediction_text=f"Error: Model expects {model.n_features_in_} features but received {features_array.shape[1]}."
            )
        
        prediction = model.predict(features_array)
        result = "Legitimate Website ✅" if prediction[0] == 0 else "Phishing Website ❌"

        return render_template("result.html", url=url, result=result)
    
    except Exception as e:
        return render_template("index.html", prediction_text=f"An error occurred: {e}")

# Run the Flask app
if __name__ == "__main__":
    phish_app.run(debug=True)
