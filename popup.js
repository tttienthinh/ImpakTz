// content.js
console.log("Content script running");


// Inject a content script into the current tab
window.onload = function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.scripting.executeScript({
            target: {tabId: tabs[0].id},
            function: getHtmlContent
        });
    });
}

// This function will be stringified and injected into the webpage
function getHtmlContent() {
    // Get the HTML content of the webpage
    const htmlContent = document.documentElement.outerHTML;

    // Parse the HTML content
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlContent, "text/html");

    // Get the title
    const title = doc.title;
    // Get the text
    const text = doc.body.textContent;

    console.log(title);

    // Send the HTML content back to the extension
    chrome.runtime.sendMessage({
        action: "htmlContent",
        content: htmlContent,
        title: title,
        text: text
    });

}


// Listen for messages from content script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log("J'ai reçu un message");
    if (message.action === "htmlContent") {
        console.log("title:", message.title, "\ntext:", message.text);
        // Do something with the HTML content
        const currencyDiv = document.querySelector('.currency');
        currencyDiv.innerHTML = '<span>New content qsdmlkfqdsimofjqdsiofiqdsfo</span>';
    }
});
