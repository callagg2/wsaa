# Web Services and Applications (WSAA)

This course explores various methods of retrieving, processing, and serving data from external and internal sources. The module covers data formats such as **XML, JSON, and CSV**, and demonstrates how to interact with APIs using **JavaScript** and **Python**.

## Project Features

*   **Data Retrieval:** Techniques for fetching data from external providers (e.g., CSO, weather servers, stock information).
*   **API Development:** Building a custom **RESTful API** using the **Flask** Python framework.
*   **CRUD Operations:** Implementation of Create, Read, Update, and Delete functionality.

### API Examples
I have developed two specific API implementations:
1.  **Books API:** A working example of a book management system that we worked on in lectures. 
    *   [Repository Link](https://github.com/callagg2/deploytopythonanywhere)
2.  **Cycle Routes API:** An adaptation of the book API logic applied to cycling routes data.
    *   [Repository Link](https://github.com/callagg2/deploytopythonanywhere2)

---

## Deployment Instructions

To deploy these applications (e.g., on [PythonAnywhere](https://www.pythonanywhere.com)), you will need to upload the following files:

| File Type | Filenames |
| :--- | :--- |
| **Python Logic** | `server.py`, `DAO.py` |
| **Frontend** | `index.html`, `api.js`, `api.css` |

### Database Configuration
The `DAO.py` file relies on a configuration object for database connectivity. If hosting elsewhere, ensure a config file exists with the following structure:
```python
config_details = {
    "host": "callagg2.mysql.pythonanywhere-services.com",
    "user": "root",
    "password": "wsaaproject",
    "database": "callagg2$wsaa"
}

## Testing and Data Analysis 
In the [`/project` directory](https://github.com/callagg2/wsaa/tree/main/project), you will find scripts used for component testing. 

A key file is `testing_downloading_from_API.py`. This script demonstrates how to: * **Download route information** directly from the API. * **Perform data processing** (e.g., calculating average distance or elevation for a specific group of routes). 
