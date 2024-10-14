inputBTL = document.querySelector(".border-top-left");
inputBTR = document.querySelector(".border-top-right");
inputBBL = document.querySelector(".border-bottom-left");
inputBBR = document.querySelector(".border-bottom-right");
previewBlock = document.querySelector(".preview-block");

updateBorderRadius = (event) => {
    isEmpty = (input) => {
        return input.value === "" ? 0 : input.value
    };
    previewBlock.style.cssText = `border-radius: ${isEmpty(inputBTL)}px ${isEmpty(inputBTR)}px ${isEmpty(inputBBR)}px ${isEmpty(inputBBL)}px;`;
};
document.addEventListener("input", updateBorderRadius);