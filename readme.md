# REST Ingest Data API

## Overview

The **REST Ingest Data API** is a FastAPI-based solution for managing data ingestion, schema registration, and contract management. It is designed to handle data ingestion at scale with efficient routing, contract validation, and integration with different route of storage layers.

## Features

- **Data Ingestion**: Supports ingestion of data payloads with contract validation.
- **Schema Management**: Allows registration and retrieval of data schemas.
- **Contract Management**: Facilitates the registration and retrieval of data contracts.
- **Health Check**: Provides a health endpoint to verify the status of the application.

## Endpoints
- **POST** /api/v1/data/ingest: Ingests data payload with contract validation.
- **POST** /api/v1/schema/register: Registers a new schema.
- **GET** /api/v1/schema/get/{schema_name}: Retrieves schema details.
- **POST** /api/v1/contract/register: Registers a new contract.
- **GET** /api/v1/contract/get/{contract_name}: Retrieves contract details.
- **GET** /api/v1/health: Health check endpoint.

## API Flow (Draft)
![Untitled diagram-2024-10-28-145704](https://github.com/user-attachments/assets/89a11db4-062d-4044-b097-02e2d5859e31)


## How to Run

1. Clone the repository and install dependencies from `requirements.txt`.
2. Run the application using Uvicorn:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
