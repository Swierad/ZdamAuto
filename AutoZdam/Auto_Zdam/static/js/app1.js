// offer adder at index

const btn1 = document.querySelector(".btn-1");

const btn2 = document.querySelector(".btn-2");
// const btn1Back = document.querySelector(".btn-1-back");

// const btn3 = document.querySelector(".btn-3");
// const btn2Back = document.querySelector(".btn-2-back");

// const btn3 = document.querySelector(".btn-3");
// const btn2Back = document.querySelector(".btn-2-back");

const div1 = document.querySelector(".div-offer-1");
const div2 = document.querySelector(".div-offer-2");
const div3 = document.querySelector(".div-offer-3");
const div4 = document.querySelector(".div-offer-4");

btn1.addEventListener("click", function () {

  div1.style.display = "none";
  div2.style.display = "block";
});

btn2.addEventListener("click", function () {

    div2.style.display = "none";
    div3.style.display = "block";
  });

// btn3.addEventListener("click", function () {

//     div3.style.display = "none";
//     div4.style.display = "block";
// });
// z
// btn1Back.addEventListener("click", function () {

//       div1.style.display = "block";
//       div2.style.display = "none";
//     });

