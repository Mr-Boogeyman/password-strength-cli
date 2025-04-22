#!/usr/bin/env python3
import argparse
from strength import evaluate_strength
from breach_check import check_breach

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("password", help="Password to check")
    args = parser.parse_args()
    
    password = args.password
    print(f"Password: {password}")
    
    score = evaluate_strength(password)
    print(f"Strength Score: {score}/100")

    if check_breach(password):
        print("Warning: This password has been breached!")
    else:
        print("✅ This password was not found in known breaches.")

if __name__ == "__main__":
    main()
