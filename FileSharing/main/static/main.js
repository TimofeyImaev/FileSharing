document.querySelector('#file_input').oninput = function(){
	let file = this.files[0];
	document.querySelector('.input-file-text').textContent = file.name;
};