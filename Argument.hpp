#ifndef ARGUMENT_HPP
# define ARGUMENT_HPP

#include <iostream>

class Argument
{
public:
	enum type{REG, DIR, IND};

	Argument(type t, int val);
	Argument(Argument const &ori);
	~Argument(void);

	Argument	&operator=(Argument const &rhs);

	type	getType(void) const;
	int		getVal(void) const;

	void	mutate(void);
private:
	Argument(void);

	Argument::type	_type;
	int				_val;
};

std::ostream& operator<<(std::ostream& o, Argument const &rhs);

#endif