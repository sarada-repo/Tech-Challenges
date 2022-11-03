
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("<NAME>.json")
  project = "<PROJECT_ID>"
  region  = "us-central1"
}

resource “google_sql_database_instance” “instance” {
name = "testinstance"
database_version = "MYSQL_8_0"
region = "us-central-1"

settings {
tier = "db-n1-standard-1"
}

}

resource "google_sql_database" “database” {
name = "testdatabase"
instance = google_sql_database_instance.instance.name
}

resource "google_sql_user" "users" {
name = "test"
instance = google_sql_database_instance.instance.name
host = "xyz"
password = var.password
sensitive = "true"
}