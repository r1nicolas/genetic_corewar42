#include "Argument.hpp"

Argument::Argument(void): _type(REG), _val(1)
{
}

Argument::Argument(Argument::type t, int val): _type(t), _val(val)
{
	if (t == REG)
		this->_val = this->_val % 16 + 1;
}

Argument::Argument(Argument const &ori): _type(ori._type), _val(ori._val)
{
}

Argument::~Argument(void)
{
}

Argument		&Argument::operator=(Argument const &rhs)
{
	this->_type = rhs._type;
	this->_val = rhs._val;
	return (*this);
}

Argument::type	Argument::getType(void) const
{
	return (this->_type);
}

int				Argument::getVal(void) const
{
	return (this->_val);
}
	
void			Argument::mutate(void)
{
		//\\
	   //  \\
	  //    \\
	 //      \\
	//        \\
   //          \\
  //            \\
 //              \\
// NOT EMPTY NOW  \\
}

std::ostream&	operator<<(std::ostream& o, Argument const &rhs)
{
	if (rhs.getType() == Argument::REG)
		o << 'r';
	else if (rhs.getType() == Argument::DIR)
		o << '%';
	o << rhs.getVal();
	return (o);
}