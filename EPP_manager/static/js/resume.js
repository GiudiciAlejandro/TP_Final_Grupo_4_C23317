
// scripts for resume page
function fn_in_stock() {
    console.log('div_in_stock');
    var obj_in_stock = document.getElementById('div_in_stock');
    var obj_assigned = document.getElementById('div_assigned');
    var obj_to_expire = document.getElementById('div_to_expire');
    var obj_to_inspect = document.getElementById('div_to_inspect');
    var obj_employees = document.getElementById('div_employees');
    obj_in_stock.style.display = 'block';
    obj_assigned.style.display = 'none';
    obj_to_expire.style.display = 'none';
    obj_to_inspect.style.display = 'none';
    obj_employees.style.display = 'none';


}

function fn_assigned() {
    console.log('div_assigned');
    var obj_in_stock = document.getElementById('div_in_stock');
    var obj_assigned = document.getElementById('div_assigned');
    var obj_to_expire = document.getElementById('div_to_expire');
    var obj_to_inspect = document.getElementById('div_to_inspect');
    var obj_employees = document.getElementById('div_employees');
    obj_in_stock.style.display = 'none';
    obj_assigned.style.display = 'block';
    obj_to_expire.style.display = 'none';
    obj_to_inspect.style.display = 'none';
    obj_employees.style.display = 'none';

}

function fn_to_expire() {
    console.log('div_expiran');
    var obj_in_stock = document.getElementById('div_in_stock');
    var obj_assigned = document.getElementById('div_assigned');
    var obj_to_expire = document.getElementById('div_to_expire');
    var obj_to_inspect = document.getElementById('div_to_inspect');
    var obj_employees = document.getElementById('div_employees');
    obj_in_stock.style.display = 'none';
    obj_assigned.style.display = 'none';
    obj_to_expire.style.display = 'block';
    obj_to_inspect.style.display = 'none';
    obj_employees.style.display = 'none';

}

function fn_to_inspect() {
    console.log('div_inspecciones');
    var obj_in_stock = document.getElementById('div_in_stock');
    var obj_assigned = document.getElementById('div_assigned');
    var obj_to_expire = document.getElementById('div_to_expire');
    var obj_to_inspect = document.getElementById('div_to_inspect');
    var obj_employees = document.getElementById('div_employees');
    obj_in_stock.style.display = 'none';
    obj_assigned.style.display = 'none';
    obj_to_expire.style.display = 'none';
    obj_to_inspect.style.display = 'block';
    obj_employees.style.display = 'none';

}

function fn_employees() {
    console.log('div_empleados');
    var obj_in_stock = document.getElementById('div_in_stock');
    var obj_assigned = document.getElementById('div_assigned');
    var obj_to_expire = document.getElementById('div_to_expire');
    var obj_to_inspect = document.getElementById('div_to_inspect');
    var obj_employees = document.getElementById('div_employees');
    obj_in_stock.style.display = 'none';
    obj_assigned.style.display = 'none';
    obj_to_expire.style.display = 'none';
    obj_to_inspect.style.display = 'none';
    obj_employees.style.display = 'block';
  
}

window.onload = function () {
    fn_in_stock();
}