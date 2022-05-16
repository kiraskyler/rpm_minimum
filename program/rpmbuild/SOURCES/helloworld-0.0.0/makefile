TARGET	:=helloworld

CC		:=gcc
CFLAGS	:=-std=c99 -O0

OBJS	:=helloworld.o

$(TARGET)	:$(SRCS)

$(OBJS)		:

.PHONY	:clean
clean 	:
	@rm $(OBJS) $(TARGET)

.PHONY :install
install :$(TARGET)
	echo "make install in $(DESTDIR) <<<<<<<<<<<<"
	sudo cp $(TARGET) $(DESTDIR)/
	sudo chmod +x $(DESTDIR)/$(TARGET)