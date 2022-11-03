resource "google_app_engine_application" "app" {
  project     = ""
  location_id = ""
}
 
resource "google_app_engine_standard_app_version" "app_v1" {
  version_id = "v1"
  service    = "default"
  runtime    = "python3.0"

 depends_on   = google_storage_bucket_object.zip
 
  deployment {
    zip {
      source_url = "https://storage.googleapis.com/pathofzip"
    }
  }

data "archive_file" "source" {
    type        = "zip"
    source_dir  = "../challenge1"
    output_path = "/tmp/appcode.zip"
}

resource "google_storage_bucket_object" "zip" {
    source       = data.archive_file.source.output_path
    content_type = "application/zip"
}
 