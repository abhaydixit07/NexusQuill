# NexusQuill

NexusQuill is a simple Flask web application for displaying blog posts and allowing users to contact the site owner via email.

## Prerequisites

Before running the application, make sure you have Python and Flask installed.

## Installation

1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.

## Configuration

Make sure to update the following variables in `app.py`:
- `PASSWORD`: Password for the email account used for sending messages.
- `EMAIL`: Email address for sending messages.

## Usage

Run the Flask application by executing `python app.py` in your terminal. By default, the application runs in debug mode.

Access the application in your web browser at `http://localhost:5000`.

## Endpoints

- `/`: Home page displaying blog posts.
- `/about`: About page.
- `/contact`: Contact page with a form for sending messages.
- `/form-entry`: Endpoint for receiving form data.
- `/post/<int:num>`: Page displaying a specific blog post identified by its ID.

## External APIs

This application uses the Unsplash API for fetching images. You can find more information about it [here](https://www.npoint.io/docs/2e4a0e1ee10447867a0d).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
