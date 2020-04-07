
console.log('Extension is loading');

chrome.runtime.onMessage.addListener(gotMessage);

function gotMessage(message, sender, sendResponse) {
  console.log(message.txt);
  if (message.txt === 'Get Paragraph') {
    let paragraphs = document.getElementsByTagName('p');
    for (paragraph of paragraphs) {
      console.log("here are the paragraph", paragraph)
    }
  }
}
