export default (match, replace, str) => {
	return str.replace(new RegExp(match, 'g'), () => replace);
};
