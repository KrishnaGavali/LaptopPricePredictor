import pandas as pd
import pickle

with open("random_forest_model.pkl", "rb") as f:
    loadmodel = pickle.load(f)

input_data_dict = {
    "os_bit": 0,
    "Touchscreen": 0,
    "msoffice": 0,
    "brand_APPLE": 0,
    "brand_ASUS": 0,
    "brand_Avita": 0,
    "brand_DELL": 0,
    "brand_HP": 0,
    "brand_Lenovo": 0,
    "brand_MSI": 0,
    "brand_acer": 0,
    "processor_brand_AMD": 0,
    "processor_brand_Intel": 0,
    "processor_brand_M1": 0,
    "processor_name_Celeron Dual": 0,
    "processor_name_Core i3": 0,
    "processor_name_Core i5": 0,
    "processor_name_Core i7": 0,
    "processor_name_Core i9": 0,
    "processor_name_M1": 0,
    "processor_name_Pentium Quad": 0,
    "processor_name_Ryzen 3": 0,
    "processor_name_Ryzen 5": 0,
    "processor_name_Ryzen 7": 0,
    "processor_name_Ryzen 9": 0,
    "processor_gnrtn_10th": 0,
    "processor_gnrtn_11th": 0,
    "processor_gnrtn_12th": 0,
    "processor_gnrtn_4th": 0,
    "processor_gnrtn_7th": 0,
    "processor_gnrtn_8th": 0,
    "processor_gnrtn_9th": 0,
    "ram_gb_16 GB": 0,
    "ram_gb_32 GB": 0,
    "ram_gb_4 GB": 0,
    "ram_gb_8 GB": 0,
    "ram_type_DDR3": 0,
    "ram_type_DDR4": 0,
    "ram_type_DDR5": 0,
    "ram_type_LPDDR3": 0,
    "ram_type_LPDDR4": 0,
    "ram_type_LPDDR4X": 0,
    "ssd_0 GB": 0,
    "ssd_1024 GB": 0,
    "ssd_128 GB": 0,
    "ssd_2048 GB": 0,
    "ssd_256 GB": 0,
    "ssd_3072 GB": 0,
    "ssd_512 GB": 0,
    "hdd_0 GB": 0,
    "hdd_1024 GB": 0,
    "hdd_2048 GB": 0,
    "hdd_512 GB": 0,
    "os_DOS": 0,
    "os_Mac": 0,
    "os_Windows": 0,
    "graphic_card_gb_0 GB": 0,
    "graphic_card_gb_2 GB": 0,
    "graphic_card_gb_4 GB": 0,
    "graphic_card_gb_6 GB": 0,
    "graphic_card_gb_8 GB": 0,
    "weight_Casual": 0,
    "weight_Gaming": 0,
    "weight_ThinNlight": 0,
    "warranty_1 year": 0,
    "warranty_2 years": 0,
    "warranty_3 years": 0,
    "warranty_No warranty": 0,
}

osbit_data = input("Enter os bit (32 or 64): ")
if osbit_data == "32":
    input_data_dict["os_bit"] = 0
else:
    input_data_dict["os_bit"] = 1

Touchscreen_data = input("Enter touchscreen (Yes or No): ")
if Touchscreen_data == "Yes":
    input_data_dict["Touchscreen"] = 1
else:
    input_data_dict["Touchscreen"] = 0

msoffice_data = input("Enter msoffice (Yes or No): ")
if msoffice_data == "Yes":
    input_data_dict["msoffice"] = 1
else:
    input_data_dict["msoffice"] = 0

brand_data = input("Enter brand: (APPLE, ASUS, Avita, DELL, HP, Lenovo, MSI, acer) ")
if brand_data == "APPLE":
    input_data_dict["brand_APPLE"] = 1
elif brand_data == "ASUS":
    input_data_dict["brand_ASUS"] = 1
elif brand_data == "Avita":
    input_data_dict["brand_Avita"] = 1
elif brand_data == "DELL":
    input_data_dict["brand_DELL"] = 1
elif brand_data == "HP":
    input_data_dict["brand_HP"] = 1
elif brand_data == "Lenovo":
    input_data_dict["brand_Lenovo"] = 1
elif brand_data == "MSI":
    input_data_dict["brand_MSI"] = 1
elif brand_data == "acer":
    input_data_dict["brand_acer"] = 1
else:
    print("Invalid brand")

if brand_data == "APPLE":
    input_data_dict["processor_brand_M1"] = 1
else:
    processor_brand_data = input("Enter processor brand: (AMD, Intel) ")
    if processor_brand_data == "AMD":
        input_data_dict["processor_brand_AMD"] = 1
    elif processor_brand_data == "Intel":
        input_data_dict["processor_brand_Intel"] = 1
    else:
        print("Invalid brand")

if brand_data == "APPLE":
    input_data_dict["processor_name_M1"] = 1
elif processor_brand_data == "Intel":
    processor_name_data = input(
        "Enter processor name: (Celeron Dual, Core i3, Core i5, Core i7, Core i9 , Pentium Quad) "
    )
    if processor_name_data == "Celeron Dual":
        input_data_dict["processor_name_Celeron Dual"] = 1
    elif processor_name_data == "Core i3":
        input_data_dict["processor_name_Core i3"] = 1
    elif processor_name_data == "Core i5":
        input_data_dict["processor_name_Core i5"] = 1
    elif processor_name_data == "Core i7":
        input_data_dict["processor_name_Core i7"] = 1
    elif processor_name_data == "Core i9":
        input_data_dict["processor_name_Core i9"] = 1
    elif processor_name_data == "Pentium Quad":
        input_data_dict["processor_name_Pentium Quad"] = 1
    else:
        print("Invalid processor name")
elif processor_brand_data == "AMD":
    processor_name_data = input(
        "Enter processor name: (Ryzen 3, Ryzen 5, Ryzen 7, Ryzen 9) "
    )
    if processor_name_data == "Ryzen 3":
        input_data_dict["processor_name_Ryzen 3"] = 1
    elif processor_name_data == "Ryzen 5":
        input_data_dict["processor_name_Ryzen 5"] = 1
    elif processor_name_data == "Ryzen 7":
        input_data_dict["processor_name_Ryzen 7"] = 1
    elif processor_name_data == "Ryzen 9":
        input_data_dict["processor_name_Ryzen 9"] = 1
    else:
        print("Invalid processor name")
else:
    print("Invalid brand")

# Complete the rest of the input process...

# Handle processor generation input
processor_generation_data = input(
    "Enter processor generation (4th, 7th, 8th, 9th, 10th, 11th, 12th): "
)

if processor_generation_data in ["4th", "7th", "8th", "9th", "10th", "11th", "12th"]:
    input_data_dict[f"processor_gnrtn_{processor_generation_data}"] = 1
else:
    print("Invalid processor generation")

# Handle RAM GB input
ram_gb_data = input("Enter RAM size in GB (4, 8, 16, 32): ")

if ram_gb_data in ["4", "8", "16", "32"]:
    input_data_dict[f"ram_gb_{ram_gb_data} GB"] = 1
else:
    print("Invalid RAM size")

# Now proceed with the rest of the code...


# Handle RAM type input
ram_type_data = input("Enter RAM type (DDR3, DDR4, DDR5, LPDDR3, LPDDR4, LPDDR4X): ")

if ram_type_data == "DDR3":
    input_data_dict["ram_type_DDR3"] = 1
elif ram_type_data == "DDR4":
    input_data_dict["ram_type_DDR4"] = 1
elif ram_type_data == "DDR5":
    input_data_dict["ram_type_DDR5"] = 1
elif ram_type_data == "LPDDR3":
    input_data_dict["ram_type_LPDDR3"] = 1
elif ram_type_data == "LPDDR4":
    input_data_dict["ram_type_LPDDR4"] = 1
elif ram_type_data == "LPDDR4X":
    input_data_dict["ram_type_LPDDR4X"] = 1
else:
    print("Invalid RAM type")

# Handle SSD and HDD input
ssd_capacity_data = input(
    "Enter SSD capacity in GB (0, 128, 256, 512, 1024, 2048, 3072): "
)

if ssd_capacity_data in ["0", "128", "256", "512", "1024", "2048", "3072"]:
    input_data_dict[f"ssd_{ssd_capacity_data} GB"] = 1
else:
    print("Invalid SSD capacity")

hdd_capacity_data = input("Enter HDD capacity in GB (0, 512, 1024, 2048): ")

if hdd_capacity_data in ["0", "512", "1024", "2048"]:
    input_data_dict[f"hdd_{hdd_capacity_data} GB"] = 1
else:
    print("Invalid HDD capacity")

# Handle OS input
os_data = input("Enter operating system (DOS, Mac, Windows): ")

if os_data == "DOS":
    input_data_dict["os_DOS"] = 1
elif os_data == "Mac":
    input_data_dict["os_Mac"] = 1
elif os_data == "Windows":
    input_data_dict["os_Windows"] = 1
else:
    print("Invalid operating system")

# Handle graphics card input
graphic_card_data = input("Enter graphics card capacity in GB (0, 2, 4, 6, 8): ")

if graphic_card_data in ["0", "2", "4", "6", "8"]:
    input_data_dict[f"graphic_card_gb_{graphic_card_data} GB"] = 1
else:
    print("Invalid graphics card capacity")

# Handle weight input
weight_data = input("Enter laptop weight (Casual, Gaming, ThinNlight): ")

if weight_data == "Casual":
    input_data_dict["weight_Casual"] = 1
elif weight_data == "Gaming":
    input_data_dict["weight_Gaming"] = 1
elif weight_data == "ThinNlight":
    input_data_dict["weight_ThinNlight"] = 1
else:
    print("Invalid weight category")

# Handle warranty input
warranty_data = input("Enter warranty period (1 year, 2 years, 3 years, No warranty): ")

if warranty_data == "1 year":
    input_data_dict["warranty_1 year"] = 1
elif warranty_data == "2 years":
    input_data_dict["warranty_2 years"] = 1
elif warranty_data == "3 years":
    input_data_dict["warranty_3 years"] = 1
elif warranty_data == "No warranty":
    input_data_dict["warranty_No warranty"] = 1
else:
    print("Invalid warranty period")


print(input_data_dict)

print()

input_data_df = pd.DataFrame([input_data_dict])


# Use the loaded model to make predictions
prediction = loadmodel.predict(input_data_df)

print("Prediction:", prediction)
