from pipeline.extract import extract_from_excel
from pipeline.transform import contact_dataframes
from pipeline.load import load_to_excel


if __name__ == "__main__":
    # Extract
    data_frame_list = extract_from_excel("data/input")

    print(type(data_frame_list))

    # Transform
    data_frame = contact_dataframes(data_frame_list)

    print(type(data_frame))

    # Load
    load_to_excel(data_frame, "data/output", "output")