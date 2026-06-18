import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create charts folder if not exists
if not os.path.exists("charts"):
    os.makedirs("charts")

# Load Dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# Basic Information
print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------
# Product Revenue Analysis
# -------------------------

product_sales = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(
    x=product_sales.index,
    y=product_sales.values
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/revenue_by_product.png")
plt.show()

# -------------------------
# Payment Method Analysis
# -------------------------

payment = df['PaymentMethod'].value_counts()

plt.figure(figsize=(8,5))
sns.barplot(
    x=payment.index,
    y=payment.values
)

plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig("charts/payment_method.png")
plt.show()

# -------------------------
# Order Status Analysis
# -------------------------

status = df['OrderStatus'].value_counts()

plt.figure(figsize=(8,5))
sns.barplot(
    x=status.index,
    y=status.values
)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig("charts/order_status.png")
plt.show()

# -------------------------
# Referral Source Analysis
# -------------------------

referral = df['ReferralSource'].value_counts()

plt.figure(figsize=(8,5))
sns.barplot(
    x=referral.index,
    y=referral.values
)

plt.title("Referral Source Analysis")
plt.xlabel("Referral Source")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig("charts/referral_source.png")
plt.show()

print("\nProject Completed Successfully!")
print("Charts Saved in charts Folder")