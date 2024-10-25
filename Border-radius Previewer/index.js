inputBTL = document.querySelector(".border-top-left");
inputBTR = document.querySelector(".border-top-right");
inputBBL = document.querySelector(".border-bottom-left");
inputBBR = document.querySelector(".border-bottom-right");
previewBlock = document.querySelector(".preview-block");
resetButtom = document.querySelector(".text-buttom");
copyButtom = document.querySelectorAll("span.text-buttom")[1]


updateBorderRadius = (event) => {
    isEmpty = (input) => {
        return input.value === "" ? 0 : input.value
    };
    previewBlock.style.cssText = `border-radius: ${isEmpty(inputBTL)}px ${isEmpty(inputBTR)}px ${isEmpty(inputBBR)}px ${isEmpty(inputBBL)}px;`;
};

resetBorderRadius = (event) => {
    if (event.target === resetButtom){
        inputBBL.value = "";
        inputBBR.value = "";
        inputBTL.value = "";
        inputBTR.value = "";
        previewBlock.style.cssText = "border-radius: 0px 0px 0px 0px;" ;
    }

}

copyBorderRadius = (event) => {
    if (event.target == copyButtom){
        const borderRadiusValue = window.getComputedStyle(previewBlock).getPropertyValue('border-radius');
        navigator.clipboard.writeText(borderRadiusValue);
        alert("Border radius value copied!")
    }
}


document.addEventListener("input", updateBorderRadius);
document.addEventListener("click", resetBorderRadius);
document.addEventListener("click", copyBorderRadius);





