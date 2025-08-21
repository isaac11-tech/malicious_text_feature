You have been asked to build a basic data processing and analysis system that includes retrieving, processing, and storing data in the database.
The system has four main functions
.1 Retrieval - This class will receive the current connection address to the database instance, retrieve the existing data in the database, and hold it in a format of your choice (recommended dataframe
.2 Processing - This class will use the information that came from the retrieval object (recommended dataframe).
Several processing and calculation operations must be performed on the texts.
If necessary, new data fields must be created with information about the texts (extraction feature, engineering and augmentation)
Each operation will create a new data field for the given text.
The required actions:
● Finding the rarest word in each text
● Finding the sentiment of the text - positive, negative or neutral (a code snippet will be provided for this action)
● Finding weapon names according to a blacklist (given a word file).
This class will also save the data in a format of your choice (dataframe is recommended).

3. Management - This class will manage the retrieval and processing operations, it will take care of transferring the information between the different objects, and will also take care of the method that accesses the information to the user.

4. Processed information access service The entire system must be wrapped in a fastapi server. This service exposes an endpoint for a GET request to receive a Jason with the texts and new data fields that have been produced.