// content.js
console.log("Content script running");

// Wait 1 second for the webpage to load
setTimeout(() => {
    // Get the HTML content of the webpage
    const htmlContent = document.documentElement.outerHTML;

    // Send the HTML content to the extension
    chrome.runtime.sendMessage({
        action: "htmlContent",
        content: htmlContent
    });
}, 1000);

console.log("Content script running : go");


// Inject a content script into the current tab
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.scripting.executeScript({
        target: {tabId: tabs[0].id},
        function: getHtmlContent
    });
});
// Inject a content script into the current tab
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.scripting.executeScript({
        target: {tabId: tabs[0].id},
        function: print_HW
    });
});

// This function will be stringified and injected into the webpage to console.log Hello world
function print_HW() {
    console.log("Hello world");
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

    console.log(title);

    // Send the HTML content back to the extension
    chrome.runtime.sendMessage({
        action: "htmlContent",
        content: htmlContent
    });

}

