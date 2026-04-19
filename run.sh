for i in {0..9}; do
    printf "test/input${i}.png\ntest/output${i}.png\n" | python3 assign_color.py
done
