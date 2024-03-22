// background.js
console.log("Background script running yo");

// Listen for messages from content script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log("Received message from content script:", message);
  if (message.action === "htmlContent") {
    console.log("Received HTML content from content script:", message.content);
    // Do something with the HTML content
  }
});

