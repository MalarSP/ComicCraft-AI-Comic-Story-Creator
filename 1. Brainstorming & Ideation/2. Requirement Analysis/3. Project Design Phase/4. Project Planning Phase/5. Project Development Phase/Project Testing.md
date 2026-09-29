# Project Testing

## Project Title
ComicCraft – AI Comic Story Creator

## Testing Objective

The objective of testing is to verify that all major features of the ComicCraft application work correctly.

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Open application | Application URL | ComicCraft homepage is displayed |
| Enter topic | Comic topic | Topic is accepted |
| Generate story | Valid topic | Five-panel comic story is generated |
| Generate image | Valid topic | Comic-style image is generated |
| Display output | Generated content | Story and image are displayed |
| Download PDF | Click download button | PDF file is generated |
| Download success | Successful download | Success page is displayed |

## Testing Areas

### Functional Testing
The main application functions such as story generation, image generation, and PDF download are checked.

### API Testing
The Google Gemini and Hugging Face APIs are tested to verify successful AI content generation.

### User Interface Testing
The input field, buttons, generated content, and download functionality are checked.

### Error Testing
The application is checked for missing API keys and invalid or incomplete inputs.

## Testing Result

The ComicCraft application was tested for its major functionalities, including comic story generation, image generation, display of results, and PDF download.
