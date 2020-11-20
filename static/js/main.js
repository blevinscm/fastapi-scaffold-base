const $ = (selector) => document.querySelector(selector)
const $$ = (selector) => document.querySelectorAll(selector)
const on = (elem, type, listener) => elem.addEventListener(type,listener)

on($('#toggle-left'),'click',()=>{
    $$(".start").forEach((elem) => elem.classList.toggle('closed'))
})
on($('#toggle-right'),'click',()=>{
    $$(".end").forEach((elem) => elem.classList.toggle('closed'))
})