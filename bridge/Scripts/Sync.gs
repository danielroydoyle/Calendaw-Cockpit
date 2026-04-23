/**
 * This function is triggered by the cloud. 
 * It takes the variable pushed by Clasp and injects it into the Doc.
 */
function updateDocFromTerminal() {
  // Use the ID from your Mind Map Doc
  const DOC_ID = '14PBiaqXuIHxGuL8v18EdXkKSNZDTnzB_9qIGDDry44ic9ehmacmFEP8r';
  const doc = DocumentApp.openById(DOC_ID);
  const body = doc.getBody();
  
  // Find your X-Ray Header
  const searchString = "--- Directory (X-Ray Update) ---";
  const element = body.findText(searchString);
  
  if (element && typeof LATEST_DIRECTORY_MAP !== 'undefined') {
    const headerElement = element.getElement().getParent();
    const container = body.getChildIndex(headerElement);
    
    // Remove the old content immediately following the header
    // (We remove the next paragraph to keep it fresh)
    try { body.removeChild(body.getChild(container + 1)); } catch(e) {}
    
    // Inject the fresh "Vocabulution"
    body.insertParagraph(container + 1, LATEST_DIRECTORY_MAP)
        .setFontFamily('Courier New')
        .setFontSize(9);
        
    console.log("X-Ray successfully pushed to Google Doc.");
  }
}