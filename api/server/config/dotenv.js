import dotenv from 'dotenv';
dotenv.config();

export const port = process.env.PORT || 5000;
export const db_name = process.env.DB_NAME;
export const db_username = process.env.DB_USERNAME;
export const db_password = process.env.DB_PASSWORD;
export const db_host = process.env.DB_HOST;
