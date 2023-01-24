
# vim: ft=make noexpandtab

MDEMONC_SRC = src/main.c

mdemonc: $(addprefix obj/$(shell uname -s)/,$(subst .c,.o,$(MDEMONC_SRC)))
	gcc -o $@ $^ $(shell pkg-config ncurses --libs) -lm

obj/$(shell uname -s)/%.o: %.c
	mkdir -p $(dir $@)
	gcc -o $@ -c $< $(shell pkg-config ncurses --cflags)

clean:
	rm -rf obj mdemonc

