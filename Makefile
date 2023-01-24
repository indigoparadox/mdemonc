
# vim: ft=make noexpandtab

MDEMOSNC_SRC = src/main.c

mdemosnc: $(addprefix obj/$(shell uname -s)/,$(subst .c,.o,$(MDEMOSNC_SRC)))
	gcc -o $@ $^ $(shell pkg-config ncurses --libs) -lm

obj/$(shell uname -s)/%.o: %.c
	mkdir -p $(dir $@)
	gcc -o $@ -c $< $(shell pkg-config ncurses --cflags)

clean:
	rm -rf obj mdemosnc

